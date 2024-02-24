import requests
from gtts import gTTS
from gtts.tts import log


class GTTS(gTTS):
    def __init__(self, text, lang, url_base):
        gTTS.__init__(self, text, lang=lang)
        self.url_base = url_base
        self.GOOGLE_TTS_HEADERS = {
            "Referer": self.url_base,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/47.0.2526.106 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        }

    def _prepare_requests(self):
        """Created the TTS API the request(s) without sending them.

        Returns:
            list: ``requests.PreparedRequests_``. <https://2.python-requests.org/en/master/api/#requests.PreparedRequest>`_``.
        """
        # TTS API URL
        translate_url = f'{self.url_base}/_/TranslateWebserverUi/data/batchexecute'
        text_parts = self._tokenize(self.text)
        log.debug("text_parts: %s", str(text_parts))
        log.debug("text_parts: %i", len(text_parts))
        assert text_parts, "No text to send to TTS API"

        prepared_requests = []
        for idx, part in enumerate(text_parts):
            data = self._package_rpc(part)

            log.debug("data-%i: %s", idx, data)

            # Request
            r = requests.Request(
                method="POST",
                url=translate_url,
                data=data,
                headers=self.GOOGLE_TTS_HEADERS,
            )

            # Prepare request
            prepared_requests.append(r.prepare())

        return prepared_requests


if __name__ == '__main__':
    import os

    tts = GTTS('你好，世界', lang='zh-cn', url_base='https://gt.hzchu.top')
    tts.save('helloworld.mp3')
    print(os.path.getsize('helloworld.mp3'))
