"""Create a synthetic PDF for demos; contains no copied paper or licensed graphics."""
from pathlib import Path
import fitz

p = Path(__file__).resolve().parent / 'synthetic_source.pdf'
doc = fitz.open()
pg = doc.new_page(width=595, height=842)
pg.insert_text((58, 80), 'Dynamic Mechanical Behavior of a Porous Material', fontsize=15)
pg.insert_text((60, 110), 'SYNTHETIC EXAMPLE - not a journal paper', fontsize=9)
pg.draw_rect(fitz.Rect(62, 170, 490, 360), color=(0.35, 0.35, 0.35))
pg.draw_line((83, 340), (467, 340), color=(0, 0, 0), width=1)
pg.draw_line((83, 185), (83, 340), color=(0, 0, 0), width=1)
for delta in [0, 17, 34]:
    pts = [(90, 331-delta), (160, 316-delta), (230, 260-delta), (300, 235-delta), (380, 214-delta), (462, 225-delta)]
    sh=pg.new_shape(); sh.draw_polyline([fitz.Point(*xy) for xy in pts]); sh.finish(color=(0.2,0.3+delta/100,0.6), width=1.5); sh.commit()
pg.insert_text((178, 385), 'Figure 1: Synthetic response curves', fontsize=10)
pg.draw_rect(fitz.Rect(100, 391, 445, 442), color=(0.45, 0.45, 0.45))
pg.insert_text((145, 418), 'sigma = F / A                  (1)', fontsize=14)
pg.insert_text((110, 482), 'Table 1: Synthetic values', fontsize=11)
pg.draw_rect(fitz.Rect(72, 500, 490, 603), color=(0.35, 0.35, 0.35))
for y in (532, 565): pg.draw_line((72, y), (490, y), color=(0.4,0.4,0.4))
pg.draw_line((270, 500), (270, 603), color=(0.4,0.4,0.4))
for y,x,t in [(520,105,'density'), (520,300,'strength'), (551,105,'400'), (551,300,'0.42'), (585,105,'600'), (585,300,'0.75')]: pg.insert_text((x,y),t,fontsize=11)
doc.save(p);doc.close()
print(p)
