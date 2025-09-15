@echo off
REM ==== Auto deploy Reflex site to GitHub Pages (Windows) ====

REM Set project path
set PROJECT_DIR=C:\path\to\Personal-Portfolio-Website-Design
set USERNAME=PreciousGian

REM Navigate to project folder
cd /d "%PROJECT_DIR%"

REM Step 1: Export static frontend
echo Exporting Reflex build...
reflex export --frontend-only

REM Step 2: Commit frontend build
echo Committing frontend build...
git add frontend
git commit -m "Auto deploy static frontend build" 2>nul

REM Step 3: Check if gh-pages branch exists
git show-ref --verify --quiet refs/heads/gh-pages
if %errorlevel%==0 (
    echo gh-pages branch exists, pushing build...
    git subtree push --prefix frontend origin gh-pages
) else (
    echo gh-pages branch does not exist, creating it...
    git checkout --orphan gh-pages
    git reset
    xcopy frontend\*.* . /s /e /y
    git add .
    git commit -m "Initial gh-pages commit"
    git push origin gh-pages --force
    git checkout main
)

echo.
echo ✅ Deployment finished!
echo Your site should be live at:
echo https://%USERNAME%.github.io/Personal-Portfolio-Website-Design/
pause
