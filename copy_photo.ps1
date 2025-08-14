# PowerShell script to quickly copy your profile photo or logo
# Usage: .\copy_photo.ps1 "path\to\your\photo.jpg"
# Usage: .\copy_photo.ps1 "path\to\your\logo.png" -IsLogo

param(
    [Parameter(Mandatory=$false)]
    [string]$PhotoPath,
    [Parameter(Mandatory=$false)]
    [switch]$IsLogo
)

$targetDir = "static\images"

if ($IsLogo) {
    $targetFile = "logo-portfolio.png"
    $fileType = "logo/favicon"
} else {
    $targetFile = "venkat-profile.jpg" 
    $fileType = "profile photo"
}

$targetPath = Join-Path $targetDir $targetFile

Write-Host "🖼️  $fileType Copy Tool" -ForegroundColor Cyan
Write-Host "=" * 40 -ForegroundColor Gray

# Create target directory if it doesn't exist
if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    Write-Host "📁 Created directory: $targetDir" -ForegroundColor Green
}

# If no photo path provided, look for common image files
if (-not $PhotoPath) {
    Write-Host "🔍 Looking for image files in current directory..." -ForegroundColor Yellow
    
    if ($IsLogo) {
        $imageFiles = Get-ChildItem -Path "." -Include "*.png","*.PNG","*logo*","*icon*" -File
    } else {
        $imageFiles = Get-ChildItem -Path "." -Include "*.jpg","*.jpeg","*.png","*.JPG","*.JPEG","*.PNG" -File
    }
    
    if ($imageFiles.Count -eq 0) {
        Write-Host "❌ No image files found in current directory" -ForegroundColor Red
        Write-Host ""
        Write-Host "💡 Usage options:" -ForegroundColor Cyan
        if ($IsLogo) {
            Write-Host "   1. .\copy_photo.ps1 `"path\to\your\logo.png`" -IsLogo"
            Write-Host "   2. Copy your logo to this directory first, then run: .\copy_photo.ps1 -IsLogo"
            Write-Host "   3. Manually save your logo as: $targetPath"
        } else {
            Write-Host "   1. .\copy_photo.ps1 `"path\to\your\photo.jpg`""
            Write-Host "   2. Copy your photo to this directory first, then run: .\copy_photo.ps1"
            Write-Host "   3. Manually save your photo as: $targetPath"
        }
        exit 1
    }
    
    Write-Host "📸 Found image files:" -ForegroundColor Green
    for ($i = 0; $i -lt $imageFiles.Count; $i++) {
        $file = $imageFiles[$i]
        $sizeKB = [math]::Round($file.Length / 1KB, 1)
        Write-Host "   $($i + 1). $($file.Name) ($sizeKB KB)" -ForegroundColor White
    }
    
    Write-Host ""
    $choice = Read-Host "Enter number to select image (or press Enter to cancel)"
    
    if ($choice -and $choice -match '^\d+$') {
        $index = [int]$choice - 1
        if ($index -ge 0 -and $index -lt $imageFiles.Count) {
            $PhotoPath = $imageFiles[$index].FullName
        } else {
            Write-Host "❌ Invalid selection" -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host "⏹️  Cancelled by user" -ForegroundColor Yellow
        exit 0
    }
}

# Check if source file exists
if (!(Test-Path $PhotoPath)) {
    Write-Host "❌ File not found: $PhotoPath" -ForegroundColor Red
    exit 1
}

# Copy the file
try {
    Copy-Item -Path $PhotoPath -Destination $targetPath -Force
    Write-Host "✅ Successfully copied $fileType to: $targetPath" -ForegroundColor Green
    
    $sourceFile = Get-Item $PhotoPath
    $targetFileInfo = Get-Item $targetPath
    $sizeKB = [math]::Round($targetFileInfo.Length / 1KB, 1)
    
    Write-Host "📊 File info:" -ForegroundColor Cyan
    Write-Host "   Source: $($sourceFile.Name)" -ForegroundColor White
    Write-Host "   Target: $($targetFileInfo.Name)" -ForegroundColor White
    Write-Host "   Size: $sizeKB KB" -ForegroundColor White
    
    Write-Host ""
    Write-Host "🚀 Next steps:" -ForegroundColor Green
    Write-Host "   1. Run: python app.py" -ForegroundColor White
    Write-Host "   2. Visit: http://localhost:5000" -ForegroundColor White
    if ($IsLogo) {
        Write-Host "   3. Your logo should now appear in browser tab and navigation!" -ForegroundColor White
    } else {
        Write-Host "   3. Your photo should now be visible in hero and about sections!" -ForegroundColor White
    }
    
} catch {
    Write-Host "❌ Error copying file: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
