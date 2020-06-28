from utils import rouge_eval, rouge_log


rouge_ref_dir = 'logs/pku_all_vocab/decode_test_50maxenc_4beam_6mindec_50maxdec_ckpt-123230/reference_tmp'
rouge_dec_dir = 'logs/pku_all_vocab/decode_test_50maxenc_4beam_6mindec_50maxdec_ckpt-123230/decoded_tmp'
print("Decoder has finished reading dataset for single_pass.")
print("Now starting ROUGE eval...")
results_dict = rouge_eval(rouge_ref_dir, rouge_dec_dir)
rouge_log(results_dict, 'logs/pku_all_vocab/decode_test_50maxenc_4beam_6mindec_50maxdec_ckpt-123230/')
