import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
const require = createRequire(import.meta.url);
const dest = path.resolve('app/static/vendor');
fs.mkdirSync(dest, {recursive:true});
for (const [source,name] of [['gsap/dist/gsap.min.js','gsap.min.js'],['gsap/dist/ScrollTrigger.min.js','ScrollTrigger.min.js'],['lenis/dist/lenis.js','lenis.js']]) {
  fs.copyFileSync(require.resolve(source), path.join(dest,name));
}
for (const [pkg,file] of [['gsap','README.md'],['lenis','LICENSE']]) {
  const root=path.resolve('node_modules',pkg);
  fs.copyFileSync(path.join(root,file),path.join(dest,pkg+'-'+file));
}
console.log('Animation libraries copied to app/static/vendor.');
