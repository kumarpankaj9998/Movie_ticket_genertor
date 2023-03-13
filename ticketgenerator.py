from PIL import Image, ImageDraw, ImageFont
ticket_width = 600
ticket_height = 400
background = Image.new(
    'RGBA', (ticket_width, ticket_height), (255, 255, 255, 255))
poster = Image.open('/content/841d3f6bbd8fef0ed41021c7b2d5cca8.jpg')
poster = poster.resize((200, 300))
background.paste(poster, (50, 50))
logo = Image.open('/content/logo_movie.png')
logo = logo.resize((80, 80))
background.paste(logo, (50, 275))
qr_image = Image.open('/content/istockphoto-828088276-612x612.jpg')
qr_image = qr_image.resize((70, 70))
background.paste(qr_image, (520, 275))
title = "Joker"
date = "March 10, 2023"
time = "8:00 PM"
theater = "AMC Theaters"
font = ImageFont.truetype('LiberationSans-Regular.ttf', 36)
draw = ImageDraw.Draw(background)
draw.text((300, 50), title, font=font, fill=(0, 0, 0, 255))
draw.text((300, 100), date, font=font, fill=(0, 0, 0, 255))
draw.text((300, 150), time, font=font, fill=(0, 0, 0, 255))
draw.text((300, 200), theater, font=font, fill=(0, 0, 0, 255))
background.save('/content/sample_data/movie_ticket.png')
