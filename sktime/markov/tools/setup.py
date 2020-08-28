from pathlib import Path


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('tools', parent_package, top_path)

    config.add_subpackage('analysis')
    config.add_subpackage('analysis.dense')
    config.add_subpackage('analysis.sparse')

    config.add_subpackage('estimation')

    config.add_subpackage('flux')
    config.add_subpackage('flux.dense')
    config.add_subpackage('flux.sparse')

    config.add_subpackage('generation')

    config.add_extension('kahandot',
                         sources=['kahandot/kahandot_module.cpp'],
                         include_dirs=[Path(top_path) / 'sktime' / 'src' / 'include'],
                         language='c++')

    return config
