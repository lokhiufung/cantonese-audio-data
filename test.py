from utils import get_jyutping_from_api, get_logger

logger = get_logger('jyutping', fh_lv='debug', ch_lv='error', logger_lv='debug')
missing_chars = {'撚', '蹟', '昶', '槿', '彊', '硤', '髀', '樑', '痾', '唪', '煬', '閑', '裏', '嘭', '㗎', '烚', '鷓', '㖭', '琨', '喼', '唔', '萼', '喺', '嘢', '砲', '嚙', '曱', '喎', '鎚', '鴣', '揼', '噃', '幪', '阪', '冚', '睇', '諗', '乜', '攰', '呔', '㩒', '慳', '嗌', '鎔', '邨', '&', '嘥', '煒', '脷', '啖', '証', '埗', '噏', '鏵', '嚿', '暐', '喳', '啫', '祚', '喑', '潯', '咩', '掟', '攞', '哋', '咗', '嗰', '咁', '佢', '嗱', '𨋢', '啱', '偈', '梘', '槤', '戥', '韞', '衞', '掹', '抆', '嘆', '畀', '孭', '喐', '嘅', '糉', '劏', '孖', '揸', '氹', '檯', '煲', '叻', '埸', '撳', '呃', '黐', '櫈', '饑', '盃', '濠', '瞓', '嚟', '剷', '甴', '鈎', '薌', '冇', '壆', '軚', '屙', '冧', '啲', '瑭', '臺', '拎', '俾', '唥', '嬲'}

outputs = []
for char in missing_chars:
    try:
        result = get_jyutping_from_api(char)
        outputs.append(char + ' ' + result)
    except:
        logger.error(char)

content = '\n'.join(outputs)
with open('results.txt', 'w') as f:
    f.write(content)    