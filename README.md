# Wild Animals Website

A simple, static website showcasing animals with photos, sounds, and videos. Perfect for GitHub Pages hosting.

## 🚀 Quick Start

1. Fork this repository
2. Enable GitHub Pages in Settings → Pages → Source: Deploy from a branch → main
3. Your site will be available at `https://yourusername.github.io/repositoryname`

## 📁 Project Structure

```
/
├── index.html              # Home page with animal grid
├── style.css              # Main stylesheet
├── assets/
│   ├── images/animals/    # Animal photos (tiger.jpg, elephant.jpg, etc.)
│   └── audio/            # Animal sounds (tiger.mp3, elephant.mp3, etc.)
├── animals/
│   ├── tiger.html        # Individual animal pages
│   ├── elephant.html
│   └── lion.html
├── templates/
│   ├── animal_page.html      # Template for individual pages
│   └── index.html           # Template for home page
├── data/
│   ├── animals.json     # Animal data (EDIT THIS FILE)
│   └── animals.js       # JavaScript version (for compatibility)
└── generate_pages.py    # 🤖 Page generator script
```

## ➕ Adding a New Animal (Automated Way - Recommended!)

### Step 1: Add Animal Data
Edit `data/animals.json` and add your new animal:

```json
{
    "existing animals...": "...",
    
    "zebra": {
        "name": "ZEBRA",
        "scientific": "equus quagga",
        "image": "assets/images/animals/zebra.jpg",
        "audio": "assets/audio/zebra.mp3",
        "youtube": "https://youtube.com/watch?v=YOUR_VIDEO_ID",
        "description": "Your zebra description here..."
    }
}
```

### Step 2: Add Files
1. **Photo**: Add `zebra.jpg` to `assets/images/animals/` folder
2. **Audio**: Add `zebra.mp3` to `assets/audio/` folder (optional)

### Step 3: Generate All Pages
Run the generator script:
```bash
python3 generate_pages.py
```

That's it! ✨ The script will automatically:
- Generate `animals/zebra.html` with animations
- Update `index.html` with the new animal card
- Check if your image/audio files exist
- Show warnings for any missing files

## 🤖 Manual Way (Old Method)
If you prefer manual editing, you can still:
1. Copy any existing HTML file from `animals/` folder  
2. Rename it and update all content manually
3. Update `index.html` manually

But the generator is much easier! 🎯

## 🎵 Audio Files

- Supported formats: MP3, WAV, OGG
- Recommended: MP3 files under 5MB
- Place audio files in `assets/audio/` folder
- Reference them in `animals.js` as `"assets/audio/filename.mp3"`

## 🖼️ Image Guidelines

- **Format**: JPG or PNG
- **Size**: Recommended 1920x1080px for hero images
- **File size**: Under 2MB for faster loading
- **Naming**: Use lowercase, no spaces (e.g., `african_elephant.jpg`)

## 🎬 YouTube Videos

1. Get the video ID from any YouTube URL:
   - `https://youtube.com/watch?v=dQw4w9WgXcQ` → ID is `dQw4w9WgXcQ`
2. Use the full URL in your `animals.js` file

## 🎨 Customization

### Colors
Edit `style.css` to change the color scheme:
- Primary accent: `#ff6b35` (orange buttons)
- Background: Dark gradient from `#1a1a1a` to `#2d2d2d`

### Text
- All animal names are automatically uppercase
- Scientific names are automatically lowercase and italic
- Descriptions should be 2-3 sentences for best display

## 🌐 GitHub Pages Setup

1. Go to your repository settings
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Click "Save"
6. Your site will be live in a few minutes!

## 🔧 Troubleshooting

**Images not loading?**
- Check file names match exactly (case-sensitive)
- Ensure files are in the correct folder
- Try refreshing the page

**Audio not playing?**
- Verify MP3 file is in `assets/audio/` folder
- Check file size (keep under 5MB)
- Some browsers require user interaction before playing audio

**New animal not showing?**
- Check `animals.js` syntax (commas, quotes, brackets)
- Ensure the animal key matches the HTML filename
- Clear browser cache and refresh

## 📝 Tips for Non-Technical Users

- **Always test locally**: Open `index.html` in your browser before committing changes
- **Use GitHub web interface**: You can edit files directly on GitHub.com
- **One change at a time**: Make small changes and test them
- **Keep backups**: Download your working files before making major changes

## 🆘 Need Help?

- Check that all files are properly uploaded
- Ensure `animals.js` has correct syntax
- Use the browser developer console (F12) to check for errors
- Compare your new files with existing working examples