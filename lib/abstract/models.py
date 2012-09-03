from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust
from django.contrib.auth.models import User
from django.db.models.signals import post_save







def re_img_span(
	sizes = {
		lgdesk, (70, 30)
		desk = (60, 20)
		tab = (42, 20)
		
        w = (span*(div+margin)-margin)
        if span <= 3:
        	h = (w*1.2)
        else:
                h = (w*0.6)
        return w, int(round(h))





def responsive_image(rimage, span):
	#returns images cropped for responsive design, l=large desktop, d=desktop, t=tablet, none=thumbnail     
        limage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(l[0], l[1])], image_field='rimage', cache_to='cache/limage/', format='JPEG', options={'quality':90})
        dimage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(d[0], d[1])], image_field='rimage', cache_to='cache/dimage/', format='JPEG', options={'quality':90})
        timage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(t[0], t[1])], image_field='rimage', cache_to='cache/timage/', format='JPEG', options={'quality':90})
        thumbnail       = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(60, 60)], image_field='timage', cache_to='cache/thumbnails/', format='JPEG', options={'quality':90})
      
	return limage, dimage, timage, thumbnail
