#!/usr/bin/env python3
import sys
import qrcode
import qrcode.image.svg

def generate_qr_svg(url, output_path):
    """Generate a QR code SVG for the given URL."""
    # Create QR code with SVG factory
    factory = qrcode.image.svg.SvgPathImage
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        image_factory=factory
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create SVG image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to file
    with open(output_path, 'wb') as f:
        img.save(f)
    
    print(f"QR code generated: {output_path}")
    print(f"URL: {url}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_qr.py <URL> <output_path>")
        sys.exit(1)
    
    url = sys.argv[1]
    output_path = sys.argv[2]
    
    generate_qr_svg(url, output_path)
