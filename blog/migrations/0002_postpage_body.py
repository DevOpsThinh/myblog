# Generated by Django 4.0.3 on 2022-04-05 02:06

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h1', wagtail.core.blocks.CharBlock()), ('h2', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image_text', wagtail.core.blocks.StructBlock([('reverse', wagtail.core.blocks.BooleanBlock(require=False)), ('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('image_carousel', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True),
        ),
    ]
