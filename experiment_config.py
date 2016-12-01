"""Experiment configuration for SBN."""
import config

def get_config():
  """Define config and command line args."""
  cfg = config.Config()
  cfg.define_string('dtype', 'float32', 'dtype to use')
  cfg.define_boolean('eval_only', False, 'only evaluate')
  # data
  cfg.define_integer('batch_size', 20, 'batch size')
  with cfg.scope('data'):
    cfg.define_string('split', 'train', 'which split to use')
    cfg.define_string('dir', '/tmp/',
        'data directory, where the binarized_mnist.hdf5 file is'
        '(the output of make_binarized_mnist_hdf5_file.py)')
    cfg.define_integer('n_examples', 50000, 'number of datapoints')
    # cfg.define_list('shape', [1, 1, 1], 'shape of the data')
    cfg.define_list('shape', [28, 28, 1], 'shape of the data')
  # optimization
  with cfg.scope('optim'):
    cfg.define_integer('n_iterations', int(1e7), 'number of iterations')
    cfg.define_float('beta1', 0.9, 'adam beta1 parameter')
    cfg.define_float('beta2', 0.999, 'adam beta2 parameter')
    cfg.define_float('epsilon', 1e-6, 'adam eps')
    cfg.define_float('learning_rate', 0.001, 'learning rate for p')
  # model
  with cfg.scope('p'):
    cfg.define_integer('h_dim', 200, 'latent dimensionality')
    cfg.define_integer('n_layers', 3, 'number of layers')
  # variational
  with cfg.scope('q'):
    cfg.define_integer('n_samples', 5, 'number of samples')
  # logging
  with cfg.scope('log'):
    cfg.define_string('dir', '/tmp', 'output directory')
    cfg.define_boolean('clear_dir', False, 'clear output directory')
    cfg.define_integer('print_every', 100, 'print every')
  cfg.parse_args()
  return cfg
