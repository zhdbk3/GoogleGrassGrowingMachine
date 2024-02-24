from google_trans_new import google_translator
import json
import requests
from google_trans_new.constant import LANGUAGES
from google_trans_new.google_trans_new import google_new_transError

import time

DEBUG_WITHOUT_TRANSLATING = False


class GoogleTranslator(google_translator):
    def __init__(self, url_base, timeout=5, proxies=None):
        google_translator.__init__(self, timeout=timeout, proxies=proxies)
        self.url_base = url_base
        self.url = url_base + "/_/TranslateWebserverUi/data/batchexecute"

    def translate(self, text, lang_tgt='auto', lang_src='auto', pronounce=False, cookies=None):
        if DEBUG_WITHOUT_TRANSLATING:
            import random
            time.sleep(random.random())
            return text + '草'
        else:
            return self.translate_really(text, lang_tgt=lang_tgt, lang_src=lang_src, pronounce=pronounce, cookies=cookies)

    def translate_really(self, text, lang_tgt='auto', lang_src='auto', pronounce=False, cookies=None):
        try:
            lang = LANGUAGES[lang_src]
        except:
            lang_src = 'auto'
        try:
            lang = LANGUAGES[lang_tgt]
        except:
            lang_src = 'auto'
        text = str(text)
        if len(text) >= 5000:
            return "Warning: Can only detect less than 5000 characters"
        if len(text) == 0:
            return ""
        headers = {
            "Referer": self.url_base,
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/47.0.2526.106 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        # 自定义cookies
        if len(cookies) > 0:
            headers['Cookie'] = cookies
        # print(cookies)
        freq = self._package_rpc(text, lang_src, lang_tgt)
        response = requests.Request(method='POST',
                                    url=self.url,
                                    data=freq,
                                    headers=headers,
                                    )
        try:
            if self.proxies == None or type(self.proxies) != dict:
                self.proxies = {}
            with requests.Session() as s:
                s.proxies = self.proxies
                r = s.send(request=response.prepare(),
                           verify=False,
                           timeout=self.timeout)
            for line in r.iter_lines(chunk_size=1024):
                decoded_line = line.decode('utf-8')
                if "MkEWBc" in decoded_line:
                    try:
                        response = decoded_line
                        response = json.loads(response)
                        response = list(response)
                        response = json.loads(response[0][2])
                        response_ = list(response)
                        response = response_[1][0]
                        if len(response) == 1:
                            if len(response[0]) > 5:
                                sentences = response[0][5]
                            else:  ## only url
                                sentences = response[0][0]
                                if pronounce == False:
                                    return sentences
                                elif pronounce == True:
                                    return [sentences, None, None]
                            translate_text = ""
                            for sentence in sentences:
                                sentence = sentence[0]
                                translate_text += sentence.strip() + ' '
                            translate_text = translate_text
                            if pronounce == False:
                                return translate_text
                            elif pronounce == True:
                                pronounce_src = (response_[0][0])
                                pronounce_tgt = (response_[1][0][0][1])
                                return [translate_text, pronounce_src, pronounce_tgt]
                        elif len(response) == 2:
                            sentences = []
                            for i in response:
                                sentences.append(i[0])
                            if pronounce == False:
                                return sentences
                            elif pronounce == True:
                                pronounce_src = (response_[0][0])
                                pronounce_tgt = (response_[1][0][0][1])
                                return [sentences, pronounce_src, pronounce_tgt]
                    except Exception as e:
                        raise e
            r.raise_for_status()
        except requests.exceptions.ConnectTimeout as e:
            raise e
        except requests.exceptions.HTTPError as e:
            # Request successful, bad response
            raise google_new_transError(tts=self, response=r)
        except requests.exceptions.RequestException as e:
            # Request failed
            raise google_new_transError(tts=self)


if __name__ == '__main__':
    translator = GoogleTranslator('https://gt.hzchu.top')
    print(translator.translate('你好，世界', lang_src='zh-cn', lang_tgt='en'))
