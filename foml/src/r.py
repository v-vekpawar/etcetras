import matplotlib.pyplot as plt
from wordcloud import WordCloud
import warnings

def generate_keyword_wordcloud():
    """
    Generates and saves a realistic word cloud (Figure 5.3) based on
    the keyword frequencies from the training report's Table 5.4.
    """
    
    print("Generating word cloud from report data...")
    
    # --- 1. Define Statistics from Report ---
    # This data is from Table 5.4 in your report.
    # The dictionary format {word: frequency} is required.
    keyword_data = {
        'wireless': 312,
        'bluetooth': 289,
        'smart': 245,
        'led': 201,
        'portable': 190,
        'eco-friendly': 175, # wordcloud handles hyphens
        'watch': 160,
        'pro': 145,
        'gaming': 130,
        'hd': 115,
        'mini': 90,
        'audio': 85,
        'black': 80,
        'white': 78,
        'usb': 75,
        'adapter': 70,
        '4k': 68,
        'premium': 65,
        'fast': 62,
        'charge': 60,
        'headset': 55,
        'laptop': 50,
        'camera': 45,
        'power': 42,
        'bank': 40,
        'cable': 38,
        'v2': 35,
        'lite': 30
    }
    
    # --- 2. Create the WordCloud Object ---
    print("Creating WordCloud object...")
    
    # Set font to Times New Roman (to match your report)
    # This is a best-effort; it will use a default if not found.
    font_path = None
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            # Try to find a common path for Times New Roman
            # This is OS-dependent and might not work, but it's a good try.
            # On Windows: 'C:/Windows/Fonts/times.ttf'
            # On macOS: '/Library/Fonts/Times New Roman.ttf'
            # On Linux: (requires fontconfig)
            
            # A more robust way (if matplotlib knows about it):
            import matplotlib.font_manager
            font_path = matplotlib.font_manager.findfont('Times New Roman')
            print(f"Found font: {font_path}")
        except:
            font_path = None
            print("Times New Roman font not found, using default font.")

    wordcloud = WordCloud(
        width=1200, 
        height=600, 
        background_color='white',
        font_path=font_path,
        colormap='viridis',  # A professional and common color map
        max_words=50,       # Match the "Top 50" from the report
        random_state=42     # For reproducible results
    )
    
    # --- 3. Generate from Frequencies ---
    # This is the correct method when you have a dict of frequencies
    wordcloud.generate_from_frequencies(keyword_data)
    
    # --- 4. Plot and Save the Figure ---
    print("Plotting and saving figure...")
    
    plt.figure(figsize=(12, 6))
    
    # Use 'bilinear' interpolation for a smoother look
    plt.imshow(wordcloud, interpolation='bilinear')
    
    # Remove the axes
    plt.axis('off')
    
    # Add the title (using the same font if possible)
    font_properties = {}
    if font_path:
        font_properties = {'fontname': 'Times New Roman'}

    plt.title("Figure 5.3: Word Cloud of Top 50 Keywords", 
              fontsize=16, 
              weight='bold', 
              pad=20,
              **font_properties)
    
    plt.tight_layout(pad=0)
    
    # --- 5. Save the Figure ---
    output_filename = "figure_5.3_keyword_wordcloud.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    
    print(f"\nSuccessfully generated and saved plot as:\n{output_filename}")

if __name__ == "__main__":
    generate_keyword_wordcloud()
