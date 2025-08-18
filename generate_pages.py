#!/usr/bin/env python3
"""
Static Page Generator for Wild Animals Website
Reads data/animals.js and generates all HTML pages using templates.
"""

import os
import json
import re
from pathlib import Path

def parse_animals_data(data_dir):
    """Parse the animals data from JSON file."""
    json_path = data_dir / 'animals.json'
    
    if not json_path.exists():
        raise FileNotFoundError(f"animals.json not found at {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_template(template_path):
    """Read a template file."""
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_animal_page(animal_key, animal_data, template):
    """Generate an individual animal page."""
    return template.replace('{{name}}', animal_data['name']) \
                  .replace('{{scientific}}', animal_data['scientific']) \
                  .replace('{{image}}', animal_data['image']) \
                  .replace('{{audio}}', animal_data['audio']) \
                  .replace('{{youtube}}', animal_data['youtube']) \
                  .replace('{{description}}', animal_data['description']) \
                  .replace('{{key}}', animal_key)

def generate_animal_card(animal_key, animal_data):
    """Generate HTML for an animal card on the home page."""
    # Truncate description to ~120 characters
    description = animal_data['description']
    if len(description) > 120:
        description = description[:120].rsplit(' ', 1)[0] + '...'
    
    return f'''<a href="animals/{animal_key}.html" class="animal-card">
                <img src="{animal_data['image']}" alt="{animal_data['name']}" class="animal-card-image" onerror="this.src='https://via.placeholder.com/400x250/1a1a1a/ffffff?text={animal_data['name']}'">
                <div class="animal-card-content">
                    <h3>{animal_data['name']}</h3>
                    <div class="scientific">{animal_data['scientific']}</div>
                    <p>{description}</p>
                </div>
            </a>'''

def check_file_exists(file_path, file_type, animal_key):
    """Check if a file exists and warn if it doesn't."""
    if not os.path.exists(file_path):
        print(f"⚠️  Warning: {file_type} file not found for {animal_key}: {file_path}")
        return False
    return True

def generate_pages():
    """Main function to generate all pages."""
    print("🦁 Wild Animals Static Page Generator")
    print("=" * 40)
    
    # Paths
    base_dir = Path(__file__).parent
    data_dir = base_dir / 'data'
    animal_template_path = base_dir / 'templates' / 'animal_page.html'
    index_template_path = base_dir / 'templates' / 'index.html'
    animals_dir = base_dir / 'animals'
    
    # Create animals directory if it doesn't exist
    animals_dir.mkdir(exist_ok=True)
    
    try:
        # Parse animals data
        print("📖 Parsing animals data...")
        animals_data = parse_animals_data(data_dir)
        print(f"✅ Found {len(animals_data)} animals")
        
        # Read templates
        print("📄 Reading templates...")
        animal_template = read_template(animal_template_path)
        index_template = read_template(index_template_path)
        
        # Generate individual animal pages
        print("🔨 Generating animal pages...")
        for animal_key, animal_data in animals_data.items():
            print(f"   📝 Creating {animal_key}.html...")
            
            # Check if files exist
            check_file_exists(base_dir / animal_data['image'], 'Image', animal_key)
            check_file_exists(base_dir / animal_data['audio'], 'Audio', animal_key)
            
            # Generate page
            page_content = generate_animal_page(animal_key, animal_data, animal_template)
            
            # Write file
            output_path = animals_dir / f"{animal_key}.html"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(page_content)
        
        # Generate home page
        print("🏠 Generating home page...")
        animal_cards = '\n            '.join(
            generate_animal_card(key, data) for key, data in animals_data.items()
        )
        
        index_content = index_template.replace('{{animal_cards}}', animal_cards)
        
        with open(base_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print("=" * 40)
        print("✅ Generation complete!")
        print(f"📊 Generated {len(animals_data)} animal pages + 1 home page")
        print("🚀 Ready for GitHub Pages!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

def main():
    """CLI entry point."""
    success = generate_pages()
    exit(0 if success else 1)

if __name__ == "__main__":
    main()