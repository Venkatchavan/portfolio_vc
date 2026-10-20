import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const base = process.env.PORTFOLIO_PREVIEW || 'http://127.0.0.1:4400/portfolio_vc/';
const out = path.resolve(process.env.PORTFOLIO_QA_OUT || '.qa/interactions');
fs.mkdirSync(out, {recursive:true});
const browser = await chromium.launch();
const errors = [], results = [];
const axe = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
function watch(page) {
  page.on('pageerror', e => errors.push(e.message));
  page.on('requestfailed', r => errors.push(r.url() + ': ' + r.failure()?.errorText));
}
async function audit(page, name) {
  await page.addScriptTag({content:axe});
  const report = await page.evaluate(async () => {
    const axeReport=await window.axe.run(document, {runOnly:{type:'tag', values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}});
    return {
      violations:axeReport.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))})),
      overflow:document.documentElement.scrollWidth > innerWidth + 1,
      h1:document.querySelectorAll('h1').length,
      height:document.documentElement.scrollHeight
    };
  });
  fs.writeFileSync(path.join(out,name+'-audit.json'), JSON.stringify(report,null,2));
  assert.equal(report.overflow,false,name+': horizontal overflow');
  assert.equal(report.h1,1,name+': one h1');
  assert.equal(report.violations.length,0,name+': '+JSON.stringify(report.violations));
  results.push({name,...report});
}
async function shot(page,name,selector) {
  if (selector) await page.locator(selector).evaluate(el=>el.scrollIntoView({block:'start'}));
  await page.waitForTimeout(600);
  await page.screenshot({path:path.join(out,name+'.png')});
}
try {
  const context=await browser.newContext({viewport:{width:1440,height:900}});
  const page=await context.newPage();watch(page);
  await page.goto(base+'index.html');await page.waitForTimeout(1200);
  await audit(page,'desktop-home');
  await shot(page,'desktop-hero');
  await page.getByRole('button',{name:'Reason with it',exact:true}).click();
  await page.getByRole('link',{name:'Explore SanskritEval'}).waitFor();
  assert.match(await page.locator('.network-note').textContent(),/Sanskrit/);
  await shot(page,'desktop-reasoning-map');
  const pathFlow=page.locator('[data-flow=reasoning]');
  const phase1=await pathFlow.evaluate(el=>el.style.strokeDashoffset);
  await page.waitForTimeout(200);
  assert.notEqual(await pathFlow.evaluate(el=>el.style.strokeDashoffset),phase1,'network animates');
  await page.getByRole('button',{name:'Pause motion'}).click();
  const stopped=await pathFlow.evaluate(el=>el.style.strokeDashoffset);
  await page.waitForTimeout(250);
  assert.equal(await pathFlow.evaluate(el=>el.style.strokeDashoffset),stopped,'pause stops animation');
  await page.locator('[data-filter=privacy]').click();
  assert.equal(await page.locator('.project-row:visible').count(),4);
  assert.equal(await page.locator('#project-count').textContent(),'4 projects');
  await shot(page,'desktop-filtered-projects','.work-index-header');
  await page.locator('[data-filter=all]').click();
  assert.equal(await page.locator('.project-row:visible').count(),11);
  await shot(page,'desktop-featured','#projects');
  await shot(page,'desktop-study','#independent-research');
  await page.locator('#study-details summary').click();
  assert.equal(await page.locator('#study-details').getAttribute('open'),'');
  await page.locator('#study-details summary').click();
  await shot(page,'desktop-published-findings','#published-findings');
  await shot(page,'desktop-patents','#patents');
  await shot(page,'desktop-publications','#publications');
  await shot(page,'desktop-about','#experience');
  await shot(page,'desktop-contact','#contact');
  await page.getByRole('button',{name:'Switch to dark theme'}).click();
  assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
  await audit(page,'desktop-dark');
  await shot(page,'desktop-dark-hero','#home');
  await shot(page,'desktop-dark-study','#independent-research');
  await page.reload();
  assert.equal(await page.locator('html').getAttribute('data-theme'),'dark','theme persists');
  await page.getByRole('button',{name:'Switch to light theme'}).click();
  // Follow a real case-study link and verify back navigation survives the curtain.
  await page.locator('.featured-project').first().getByRole('link',{name:'Read the project'}).click();
  await page.waitForURL('**/project/h-rag-cti.html');
  await page.locator('h1').waitFor();
  assert.match(await page.locator('h1').textContent(),/H-RAG/);
  await shot(page,'desktop-case-hero');
  await audit(page,'desktop-case');
  await page.goBack();await page.waitForTimeout(600);
  assert.equal(await page.locator('.transition-panel').evaluate(el=>getComputedStyle(el).visibility),'hidden');
  await page.goto(base+'narrative_nexus.html');
  await page.locator('[data-dialog]').first().click();
  assert.equal(await page.locator('dialog[open]').count(),1);
  await shot(page,'desktop-reading-dialog');
  await audit(page,'desktop-reading-dialog');
  await page.keyboard.press('Escape');
  assert.equal(await page.locator('dialog[open]').count(),0);
  assert.equal(await page.locator('[data-dialog]').first().evaluate(el=>document.activeElement===el),true);
  for (const [name,file] of [['archive','hobby.html'],['writing','narrative_nexus.html'],['case-cmarl','project/cmarl-thesis.html'],['case-sanskrit','project/sanskrit-eval.html']]) {
    await page.goto(base+file);await page.waitForTimeout(300);
    await audit(page,'desktop-'+name);await shot(page,'desktop-'+name);
  }
  const mobile=await browser.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:1});
  const phone=await mobile.newPage();watch(phone);
  await phone.goto(base+'index.html');await phone.waitForTimeout(1200);
  await audit(phone,'mobile-home');await shot(phone,'mobile-hero');
  await phone.getByRole('button',{name:'Menu',exact:true}).click();
  assert.equal(await phone.locator('#mobile-menu').isVisible(),true);
  await shot(phone,'mobile-menu');
  await phone.locator('#mobile-menu a').last().focus();await phone.keyboard.press('Tab');
  assert.equal(await phone.locator('.menu-toggle').evaluate(el=>document.activeElement===el),true,'menu traps tab');
  await phone.keyboard.press('Escape');
  assert.equal(await phone.locator('#mobile-menu').isVisible(),false);
  assert.equal(await phone.locator('.menu-toggle').evaluate(el=>document.activeElement===el),true,'menu restores focus');
  for (const [name,id] of [['network','.network-card'],['featured','#projects'],['index','.work-index-header'],['study','#independent-research'],['published-findings','#published-findings'],['patents','#patents'],['publications','#publications'],['about','#experience'],['contact','#contact']]) await shot(phone,'mobile-'+name,id);
  for (const [name,file] of [['archive','hobby.html'],['writing','narrative_nexus.html'],['case','project/h-rag-cti.html']]) {
    await phone.goto(base+file);await phone.waitForTimeout(300);await audit(phone,'mobile-'+name);await shot(phone,'mobile-'+name);
  }
  await phone.goto(base+'narrative_nexus.html');
  await phone.locator('[data-dialog]').first().click();
  await audit(phone,'mobile-dialog');await shot(phone,'mobile-dialog');await phone.keyboard.press('Escape');
  const response=await phone.goto(base+'deep/missing/page');
  assert.equal(response.status(),404);await audit(phone,'mobile-404');await shot(phone,'mobile-404');
  const reducedContext=await browser.newContext({viewport:{width:1440,height:900},reducedMotion:'reduce'});
  const reducedPage=await reducedContext.newPage();watch(reducedPage);
  await reducedPage.goto(base+'index.html');
  assert.equal(await reducedPage.locator('.motion-toggle').isDisabled(),true);
  assert.equal(await reducedPage.locator('.network-flow').evaluate(el=>getComputedStyle(el).display),'none');
  await audit(reducedPage,'reduced');await shot(reducedPage,'reduced-hero');await shot(reducedPage,'reduced-study','#independent-research');
  // No-JS visitors can read every study value and follow all native case links.
  const plain=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
  const plainPage=await plain.newPage();
  await plainPage.goto(base+'index.html');
  assert.equal(await plainPage.locator('.project-row:visible').count(),11);
  assert.equal(await plainPage.getByRole('heading',{level:1}).isVisible(),true);
  assert.match(await plainPage.locator('.study-chart').textContent(),/6\.5%/);
  await shot(plainPage,'no-js-study','#independent-research');
  assert.deepEqual(errors,[],'browser errors and failed assets');
  fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify({status:'PASS',errors,results,checks:['network modes and meaningful links','animation and pause','project filters','study disclosures','dark theme and persistence','case navigation and back','reading dialogs and Escape','mobile focus trap','deep-path 404','reduced motion','no JavaScript']},null,2));
  console.log('PASS: '+results.length+' page/state accessibility audits; all interaction, layout and fallback checks.');
} finally {await browser.close();}
