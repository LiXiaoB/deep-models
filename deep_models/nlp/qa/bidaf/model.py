import torch
from torch import nn


class CharEmbeddingLayer(nn.Module):
    """
    Char-CNN
    """

    def __init__(self):
        ...

    def forward(self, *input: Any, **kwargs: Any):
        ...


class WordEmbeddingLayer(nn.Module):
    """
    GLOVE
    """
    def __init__(self):
        ...

    def forward(self, *input: Any, **kwargs: Any):
        ...


class AttnEmbeddingLayer(nn.Module):

    def __init__(self):
        ...

    def forward(self, *input: Any, **kwargs: Any):
        ...


class EmbeddingLayer(nn.Module):
    """
    Word/Char Embedding + Context Embedding + Attn Embedding
    """

    def __init__(self):
        ...

    def forward(self, *input: Any, **kwargs: Any):
        ...


class ModelLayer(nn.Module):

    def __init__(self):
        ...

    def forward(self, *input: Any, **kwargs: Any):
        ...


class OutputLayer(nn.Module):

    def __init__(self):
        ...

    def forward(self, *input: Any, **kwargs: Any):
        ...

