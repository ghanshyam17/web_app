import qrcode

# The URL you want the QR code to redirect to (replace with your React app URL)
url = "http://localhost:3000"  # For local development, or use your deployed URL

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of the QR code
    border=4,  # Thickness of the border
)

qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("react_app_qrcode.png")

print("QR Code generated and saved as 'react_app_qrcode.png'")
