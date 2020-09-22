from PIL import Image, ImageDraw, ImageFont


def edit_pic(picture, text):
    im = Image.open(picture)
    # Создаем объект со шрифтом
    font = ImageFont.truetype('Montserrat_bolt.ttf', size=80)
    draw_text = ImageDraw.Draw(im)
    offset = 10
    shadowColor = 'white'
    imgWidth, imgHeight = im.size

    x = imgWidth * 0.3
    y = imgHeight - imgHeight * 0.3

    for off in range(offset):
        # move right
        draw_text.text((x - off, y), text, font=font, fill=shadowColor)
        # move left
        draw_text.text((x + off, y), text, font=font, fill=shadowColor)
        # move up
        draw_text.text((x, y + off), text, font=font, fill=shadowColor)
        # move down
        draw_text.text((x, y - off), text, font=font, fill=shadowColor)
        # diagnal left up
        draw_text.text((x - off, y + off), text, font=font, fill=shadowColor)
        # diagnal right up
        draw_text.text((x + off, y + off), text, font=font, fill=shadowColor)
        # diagnal left down
        draw_text.text((x - off, y - off), text, font=font, fill=shadowColor)
        # diagnal right down
        draw_text.text((x + off, y - off), text, font=font, fill=shadowColor)
    draw_text.text(
        (x, y),
        text,
        # Добавляем шрифт к изображению
        font=font,
        fill='#1C0606')
    im.save(picture)
