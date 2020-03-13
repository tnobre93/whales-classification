from backbones.resnet_models import ResNetModels
from backbones.densenet_models import DenseNetModels
from backbones.mobilenet_models import MobileNetModels


def get_model(embedding_dim,
              num_classes,
              pretrained,
              dropout,
              image_size,
              archi,
              alpha):

    if archi.startswith('resnet'):
        model = ResNetModels(embedding_dim=embedding_dim,
                             num_classes=num_classes,
                             image_size=image_size,
                             archi=archi,
                             pretrained=pretrained,
                             dropout=dropout,
                             alpha=alpha)

    elif archi.startswith('densenet'):
        model = DenseNetModels(embedding_dim=embedding_dim,
                               num_classes=num_classes,
                               image_size=image_size,
                               archi=archi,
                               pretrained=pretrained,
                               dropout=dropout,
                               alpha=alpha)
    elif archi.startswith('mobilenet'):
        model = MobileNetModels(embedding_dim=embedding_dim,
                                num_classes=num_classes,
                                image_size=image_size,
                                archi=archi,
                                pretrained=pretrained,
                                dropout=dropout,
                                alpha=alpha)

    return model
