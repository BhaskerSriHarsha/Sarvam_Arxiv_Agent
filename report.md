# LLM Sub-4-bit Quantization: A Comprehensive Survey

## Executive Summary
The field of LLM sub-4-bit quantization has emerged as a critical research area addressing the computational and memory demands of deploying large language models. Recent advances have demonstrated that extreme compression (2-bit to 4-bit) is achievable with minimal accuracy degradation through innovative approaches including partial binarization, ternary quantization, residual refinement, and outlier-safe pre-training. These methods enable efficient deployment on resource-constrained environments while maintaining competitive performance on reasoning and language tasks.

## Thematic Analysis

### Extreme Compression Techniques
**Binary and Ternary Approaches**: The frontier of sub-4-bit quantization includes radical compression methods. PB-LLM (Partially Binarized LLM) achieves 1-bit quantization by selectively preserving salient weights at higher precision while binarizing the majority, enabling extreme compression with maintained reasoning capabilities. PTQTP introduces a novel ternary quantization approach using {-1, 0, 1} trit-planes, achieving multiplication-free additive inference that rivals 1.58-bit QAT performance with significantly faster inference speeds.

**Residual Refinement Methods**: R2Q proposes a 2-bit quantization framework using sequential 1-bit sub-quantizations forming an adaptive quantization lattice, demonstrating that extreme compression can be achieved through progressive refinement rather than direct 2-bit approximation.

### Outlier Management Strategies
**Outlier-Safe Pre-Training**: OSP introduces a paradigm shift by preventing outlier formation during training rather than post-hoc mitigation. By combining Muon optimizer, Single-Scale RMSNorm, and learnable embedding projection, OSP models exhibit near-zero excess kurtosis compared to extreme values in standard models, fundamentally improving 4-bit quantization performance.

**Token-wise Outlier Handling**: PrefixQuant addresses token-wise outliers in KV cache through a training-free prefixing mechanism, achieving significant accuracy improvements (+2.85 to +3.08 points) over existing methods while providing substantial speedup (2.16x-2.74x).

### Hardware-Aware Quantization
**Floating-Point Quantization**: LLM-FP4 pioneers 4-bit floating-point quantization for both weights and activations, overcoming limitations of integer-based PTQ methods. The approach achieves 63.1 average score on commonsense reasoning tasks with only 5.8 points below full-precision performance.

**Hardware Optimization**: Methods like QRazor introduce significant data razoring (SDR) techniques optimized for integer-based arithmetic units, enabling direct low-precision operations without decompression overhead.

## Conclusion
The current state-of-the-art in LLM sub-4-bit quantization demonstrates that extreme compression is achievable through multiple complementary approaches. The field has evolved from naive binarization attempts to sophisticated methods that address outlier formation, residual refinement, and hardware constraints. Future directions likely include unified frameworks combining these approaches, improved hardware support for ultra-low precision arithmetic, and further exploration of ternary and binary quantization paradigms. The practical deployment of sub-4-bit quantized LLMs is becoming increasingly viable, enabling efficient inference on consumer hardware while maintaining competitive performance across diverse applications.

## Surveyed Papers

* **Title:** PB-LLM: Partially Binarized Large Language Models | **Authors:** Yuzhang Shang, Zhihang Yuan, Qiang Wu, Zhen Dong | **arXiv ID:** 2310.00034
  * **Abstract Summary:** Proposes partially-binarized LLMs that achieve 1-bit quantization by preserving salient weights at higher precision while binarizing the majority, enabling extreme compression with maintained reasoning capabilities.

* **Title:** PTQTP: Post-Training Quantization to Trit-Planes for Large Language Models | **Authors:** He Xiao, Runming Yang, Qingyao Yang, Wendong Xu, Zhen Li, Yupeng Su, Zhengwu Liu, Hongxia Yang, Ngai Wong | **arXiv ID:** 2509.16989
  * **Abstract Summary:** Introduces ternary quantization using {-1, 0, 1} trit-planes that achieves multiplication-free additive inference, rivaling 1.58-bit QAT performance with 4.63x faster inference than FP16.

* **Title:** R2Q: Towards Robust 2-Bit Large Language Models via Residual Refinement Quantization | **Authors:** Jiayi Chen, Jieqi Shi, Jing Huo, Chen Wu | **arXiv ID:** 2511.21736
  * **Abstract Summary:** Develops 2-bit quantization through sequential 1-bit sub-quantizations forming an adaptive quantization lattice, consistently outperforming existing 2-bit methods across diverse benchmarks.

* **Title:** Outlier-Safe Pre-Training for Robust 4-Bit Quantization of Large Language Models | **Authors:** Jungwoo Park, Taewhoo Lee, Chanwoong Yoon, Hyeon Hwang, Jaewoo Kang | **arXiv ID:** 2506.19697
  * **Abstract Summary:** Introduces Outlier-Safe Pre-Training (OSP) that prevents outlier formation during training rather than post-hoc mitigation, achieving 35.7 average score under 4-bit quantization with only 2% training overhead.

* **Title:** PrefixQuant: Eliminating Outliers by Prefixed Tokens for Large Language Models Quantization | **Authors:** Mengzhao Chen, Yi Liu, Jiahao Wang, Yi Bin, Wenqi Shao, Ping Luo | **arXiv ID:** 2410.05265
  * **Abstract Summary:** Proposes training-free token-wise outlier isolation through KV cache prefixing, achieving +2.85 to +3.08 accuracy improvements over existing methods with 2.16x-2.74x speedup.

* **Title:** LLM-FP4: 4-Bit Floating-Point Quantized Transformers | **Authors:** Shih-yang Liu, Zechun Liu, Xijie Huang, Pingcheng Dong, Kwang-Ting Cheng | **arXiv ID:** 2310.16836
  * **Abstract Summary:** Pioneers 4-bit floating-point quantization for both weights and activations, achieving 63.1 average score on reasoning tasks with only 5.8 points below full-precision performance.

* **Title:** Qrazor: Reliable and Effortless 4-bit LLM Quantization by Significant Data Razoring | **Authors:** Dongyoung Lee, Seungkyu Choi, Ik Joon Chang | **arXiv ID:** 2501.13331
  * **Abstract Summary:** Introduces significant data razoring (SDR) technique that retains only four most salient bits, achieving performance similar or better than state-of-the-art 4-bit methods without additional fine-tuning.

* **Title:** WKVQuant: Quantizing Weight and Key/Value Cache for Large Language Models Gains More | **Authors:** Yuxuan Yue, Zhihang Yuan, Haojie Duanmu, Sifan Zhou, Jianlong Wu, Liqiang Nie | **arXiv ID:** 2402.12065
  * **Abstract Summary:** Proposes PTQ framework specifically designed for quantizing weights and KV cache, incorporating past-only quantization and two-dimensional strategies for improved attention computation.

* **Title:** ModuLoRA: Finetuning 2-Bit LLMs on Consumer GPUs by Integrating with Modular Quantizers | **Authors:** Junjie Yin, Jiahao Dong, Yingheng Wang, Christopher De Sa, Volodymyr Kuleshov | **arXiv ID:** 2309.16119
  * **Abstract Summary:** Enables finetuning 2/3/4-bit LLMs on single 24GB GPU through quantization-agnostic backward pass, supporting state-of-the-art 2-bit QuIP# and 3-bit OPTQ quantization.