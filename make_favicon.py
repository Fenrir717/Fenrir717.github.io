from PIL import Image, ImageDraw, ImageFont

sizes = [16, 32, 48, 64, 180]

for s in sizes:
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded squircle badge
    radius = int(s * 0.22)
    draw.rounded_rectangle([0, 0, s-1, s-1], radius=radius, fill=(8, 8, 10, 255))
    draw.rounded_rectangle([1, 1, s-2, s-2], radius=radius, outline=(255, 59, 29, 200), width=max(1, int(s * 0.045)))
    
    font_size = int(s * 0.48)
    try:
        font = ImageFont.truetype('impact.ttf', font_size)
    except:
        font = ImageFont.load_default()
        
    draw.text((s * 0.46, s * 0.52), 'HQ', font=font, fill=(243, 241, 234, 255), anchor='mm')
    
    # Red dot
    dot_r = max(2, int(s * 0.075))
    dot_cx = int(s * 0.80)
    dot_cy = int(s * 0.22)
    draw.ellipse([dot_cx-dot_r, dot_cy-dot_r, dot_cx+dot_r, dot_cy+dot_r], fill=(255, 59, 29, 255))
    
    if s == 32:
        img.save(r'C:\Users\thean\.gemini\antigravity\scratch\haqiqi-portfolio\favicon-32x32.png')
    elif s == 180:
        img.save(r'C:\Users\thean\.gemini\antigravity\scratch\haqiqi-portfolio\apple-touch-icon.png')
    elif s == 64:
        img.save(r'C:\Users\thean\.gemini\antigravity\scratch\haqiqi-portfolio\favicon.png')

# Save ICO file
img_ico = Image.open(r'C:\Users\thean\.gemini\antigravity\scratch\haqiqi-portfolio\favicon.png')
img_ico.save(r'C:\Users\thean\.gemini\antigravity\scratch\haqiqi-portfolio\favicon.ico', format='ICO', sizes=[(16,16), (32,32), (48,48), (64,64)])

# Generate SVG Favicon
svg_markup = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff3b1d" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#ff3b1d" stop-opacity="0.25"/>
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="16" fill="#08080a"/>
  <rect x="1.5" y="1.5" width="61" height="61" rx="14.5" fill="none" stroke="url(#borderGrad)" stroke-width="2.5"/>
  <circle cx="50" cy="14" r="4" fill="#ff3b1d"/>
  <text x="30" y="44" font-family="'Anton', 'Impact', sans-serif" font-size="30" font-weight="900" fill="#f3f1ea" text-anchor="middle" letter-spacing="-0.5">HQ</text>
</svg>'''

with open(r'C:\Users\thean\.gemini\antigravity\scratch\haqiqi-portfolio\favicon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_markup)

print('Generated favicon suite successfully!')
