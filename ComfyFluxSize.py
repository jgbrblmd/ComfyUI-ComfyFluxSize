class ComfyFluxSize:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "DimSize": (["1024x1024", "1216x832", "832x1216"],),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_size"

    CATEGORY = "sizing"

    def get_size(self, DimSize):
        width, height = map(int, DimSize.split('x'))
        return (width, height)

NODE_CLASS_MAPPINGS = {
    "ComfyFluxSize": ComfyFluxSize
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyFluxSize": "ComfyFlux Size"
}