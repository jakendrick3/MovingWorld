from diffusers import DiffusionPipeline
import torch
print("Instantiating pipeline...")
pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
print("Loading model to GPU...")
pipeline.to("cuda")
print("Generating image...")
image = pipeline("A Fantasy world map with intricate details. It should have mountain ranges, rivers, a desert, and forests.").images[0]
image.save("fantasy_world_map.png")