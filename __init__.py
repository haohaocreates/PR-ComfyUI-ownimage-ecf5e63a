from .CachingImageLoader import *

NODE_CLASS_MAPPINGS = {
    "Caching Image Loader": CachingImageLoader
}

__all__ = ['NODE_CLASS_MAPPINGS']

def do_install():
    import importlib
    spec = importlib.util.spec_from_file_location('impact_install', os.path.join(os.path.dirname(__file__), 'install.py'))
    impact_install = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(impact_install)

for x in range(12):
    print('####################################')

print('\033[34mOwnimage: \033[92mLoaded\033[0m')
print(f'CachingImageLoader: {CachingImageLoader.status()}')

for x in range(12):
    print('####################################')
