# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field
from typing import Optional

__all__ = ["ModelConfig"]


@dataclass
class ModelConfig:
    model_name_or_path: str = field(
        default=None, metadata={"help": "Build-in pretrained model name or the path to local model."}
    )
    tokenizer_name_or_path: Optional[str] = field(
        default=None, metadata={"help": "Pretrained tokenizer name or path if not the same as model_name"}
    )
    use_fast_layer_norm: bool = field(
        default=False,
        metadata={"help": "GPT3 model, use fast layernorm"},
    )
    fuse_attention_qkv: bool = field(
        default=None,
        metadata={"help": "whether to fuse attention qkv"},
    )
    fuse_attention_ffn: bool = field(
        default=None,
        metadata={"help": "whether to fuse first up and gate proj in mlp block"},
    )
    hidden_dropout_prob: float = field(default=0.1, metadata={"help": "The hidden dropout prob."})
    attention_probs_dropout_prob: float = field(default=0.1, metadata={"help": "The attention hidden dropout prob."})

    continue_training: bool = field(
        default=True,
        metadata={
            "help": "Whether to train from existing paddlenlp model weights. If set True, the model_name_or_path argument must exist in the paddlenlp models."
        },
    )
    weight_quantize_algo: str = field(
        default=None,
        metadata={
            "help": "Model weight quantization algorithm including 'nf4', 'fp4','weight_only_int4', 'weight_only_int8'."
        },
    )
    weight_blocksize: int = field(
        default=64,
        metadata={"help": "Block size for weight quantization(Only available for nf4 or fp4 quant_scale.)."},
    )
    weight_double_quant: bool = field(
        default=False, metadata={"help": "Whether apply double quant(Only available for nf4 or fp4 quant_scale.)."}
    )
    weight_double_quant_block_size: int = field(
        default=256,
        metadata={
            "help": "Block size for quant_scale of weight quant_scale(Only available for nf4 or fp4 quant_scale.)"
        },
    )

    # LoRA related parameters
    lora: bool = field(default=False, metadata={"help": "Whether to use LoRA technique"})
    lora_path: str = field(default=None, metadata={"help": "Initialize lora state dict."})
    lora_rank: int = field(default=8, metadata={"help": "Lora attention dimension"})
    use_quick_lora: bool = field(
        default=False,
        metadata={
            "help": "Whether to use quick lora, The use of Quick LoRa will only take effect when lora_dropout is set to 0."
        },
    )
    rslora: bool = field(default=False, metadata={"help": "Whether to use RsLoRA"})
    lora_plus_scale: float = field(default=1.0, metadata={"help": "Lora B scale in LoRA+ technique"})
    pissa: bool = field(default=False, metadata={"help": "Whether to use Pissa: https://arxiv.org/pdf/2404.02948.pdf"})
    lora_use_mixer: bool = field(
        default=False, metadata={"help": "Whether to use MosLoRA: https://arxiv.org/pdf/2406.11909"}
    )

    # vera related parameters
    vera: bool = field(default=False, metadata={"help": "Whether to use vera technique"})
    vera_rank: int = field(default=8, metadata={"help": "Vera attention dimension"})

    # lokr related parameter
    lokr: bool = field(default=False, metadata={"help": "Whether to use LoKr technique"})
    lokr_path: str = field(
        default=None, metadata={"help": "Initialize lokr state dict and apply customized lokr config"}
    )
    lokr_dim: int = field(default=8, metadata={"help": "Lora dimention in LoKr dimension for adapter matrix"})

    # prefix tuning related parameters
    prefix_tuning: bool = field(default=False, metadata={"help": "Whether to use Prefix technique"})
    prefix_path: str = field(default=None, metadata={"help": "Initialize prefix state dict."})
    num_prefix_tokens: int = field(default=128, metadata={"help": "Number of prefix tokens"})

    # reft related parameter
    reft: bool = field(default=False, metadata={"help": "Whether using reft method"})

    from_aistudio: bool = field(default=False, metadata={"help": "Whether to load model from aistudio"})
    save_to_aistudio: bool = field(default=False, metadata={"help": "Whether to save model to aistudio"})
    aistudio_repo_id: str = field(default=None, metadata={"help": "The id of aistudio repo"})
    aistudio_repo_private: bool = field(default=True, metadata={"help": "Whether to create a private repo"})
    aistudio_repo_license: str = field(default="Apache License 2.0", metadata={"help": "The license of aistudio repo"})
    aistudio_token: str = field(default=None, metadata={"help": "The token of aistudio"})
    neftune: bool = field(default=False, metadata={"help": "Whether to apply NEFT"})
    neftune_noise_alpha: float = field(default=5.0, metadata={"help": "NEFT noise alpha"})
    flash_mask: bool = field(default=False, metadata={"help": "Whether to use flash_mask in flash attention."})

    # long sequence strategy
    use_long_sequence_strategies: bool = field(
        default=False, metadata={"help": "Whether to use long sequence strategy"}
    )
    rope_scaling_factor: float = field(default=1.0, metadata={"help": "Rope extension scaling factor"})
    strategy_type: str = field(default=None, metadata={"help": "Long sequence strategy type"})
    strategy_name: str = field(default=None, metadata={"help": "Long sequence strategy name"})
