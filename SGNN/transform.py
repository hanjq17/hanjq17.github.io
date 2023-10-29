from PIL import ImageSequence, Image
import imageio, os 

location = "img/"
gif_file = os.path.join(location, "rotation.gif")
out_file = os.path.join(location, "rotation1.gif")
frames = [frame.copy().convert("RGBA") for frame in ImageSequence.Iterator(Image.open(gif_file))]
imageio.mimsave(out_file, frames, 'GIF', duration=0.08)
