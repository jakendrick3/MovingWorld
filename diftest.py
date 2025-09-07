from diffusers import DiffusionPipeline
import torch
print("Instantiating pipeline...")
pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
print("Loading model to GPU...")
pipeline.to("cuda")
print("Generating image...")
image = pipeline("An image of a squirrel in Picasso style").images[0]
image.save("squirrel_picasso.png")