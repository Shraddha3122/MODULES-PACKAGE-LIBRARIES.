# Submodule: Filters
class FilterApplier:
    @staticmethod
    def apply_filter(image, filter_name):
        filters = {
            "BLUR": ImageFilter.BLUR,
            "CONTOUR": ImageFilter.CONTOUR,
            "DETAIL": ImageFilter.DETAIL,
            "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
            "EMBOSS": ImageFilter.EMBOSS,
            "SHARPEN": ImageFilter.SHARPEN,
        }
        if filter_name not in filters:
            raise ValueError(f"Filter {filter_name} is not supported")
        
        return image.filter(filters[filter_name])