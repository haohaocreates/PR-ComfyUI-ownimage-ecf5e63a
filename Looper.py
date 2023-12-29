
class Looper:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "original_latent": ("LATENT",),
                "loop_latent": ("LATENT",),
                "loop_count": ("INT", {"default": 10, "min": 1, "max": 100, "step": 5}),
            }
        }

    RETURN_TYPES = ("LATENT", "FLOAT", "LATENT")
    RETURN_NAMES = ("final_output_latent", "loop_fraction", "loop_latent")
    FUNCTION = "loop_action"
    CATEGORY = "ownimage"

    def loop_action(self, original_latent, loop_latent, loop_count):
        for x in range(loop_count):
            print(f'ownimage Looper: {x}')
        return original_latent, 0.5

    @classmethod
    def IS_CHANGED(self, original_latent, loop_latent, loop_count):
        print('ownimage Looper: IS_CHANGED')
        return float("NaN")