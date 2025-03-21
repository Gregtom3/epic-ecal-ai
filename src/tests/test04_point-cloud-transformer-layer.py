import torch
from point_transformer_pytorch import PointTransformerLayer

def test_layer():
    attn = PointTransformerLayer(
        dim = 128,
        pos_mlp_hidden_dim = 64,
        attn_mlp_hidden_mult = 4
    )

    feats = torch.randn(1, 16, 128)
    pos = torch.randn(1, 16, 3)
    mask = torch.ones(1, 16).bool()
    
    x=attn(feats, pos, mask = mask) # (1, 16, 128)
    print(x)
