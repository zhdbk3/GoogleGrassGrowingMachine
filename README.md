# 谷歌生草机4

## 作者

<a title="bilibili" target="_blank" href="https://space.bilibili.com/551409211"><img src="https://img.shields.io/badge/dynamic/json?color=353940&labelColor=f27596&label=Bilibili&suffix=%20followers&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dbilibili%26queryKey%3D551409211&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAD7ElEQVR4nO2dW9WrMBCFK6ESkFAJSKiESqgEHCABCZWAhEpAAhL2ecik5dDc/pXLBDLfWnlqy0xmJ5BMQnq5CIIgCIIgCIIgCIIgCEIBAHQAemYfrgCunD6wAKAHsEKxALgx+bCQD8/S9tmgVqeDr1lLigDgZvDhXso+K9TyTBQRwRJ8AHjntl0Flh5QRAQK/mKxPeayWx2OXpBNBKiHvi34b7T2MC4pAvW6twR/RwkRKPizBN8CgEcuESj4Lwm+BwBjahEk+H8EwJRKhOaCDzW8e1JLfkUUH1NgmR3XmHffHR1l+72BSs8d7w8U+JDAnZERQMcV+CtUi7dNqFqibB4J7vtrq7xKCuAasbTMXCL4T+5aVk6+2xHUrWdhruAR6HIJcOeu2UHI8zyAe2ytWfEdWz9PVvQ8YAmIQ5dDAB9LFsMVAv8oMO2zAGrC5WNIarRiAuKR9jYEd9pY08aa6uUzIHGRdkgKd8pY0yc1WjEBAqypDYoAG0QAZkQAZkQAZkQAZk4vANQenjsSzS3I/wcSbXU5jQBUkRtdf4Rar90v8kSv3+I3ffCCSpk8I/w+lgDkdI/v2rEp2CaiWm1AsDQLlDAD+dlFXLMeAaCSeLZdaSFE5VUQNot38cKuEeBgAsSuG0flVZBmEanbXfNQAsS0fgBYIn2fIu3/BBMHEyBmDXlFfA8IzeHb+Ems4WAChKykrVA9ZfsQTL57jXzRg4A5wC/A8N4ADiZAZwm2XjW75Qh2KOTfA0p4kygPw28OJcCVgn3nDnYo2EwEYRgGH0qAMyICMCMCMCMCMCMCMCMCMCMCfP3qwHDOQ4AAUekTk8FaBRihJnZdYbvtCGC7LvmkM63GjVDINPFrQgCq5ETXfmMzI90FXzPvfqt7x4rEu/ZaEcCUxFvgz2zO+BUn6UkoaEEAsptiMSX5e8FoRYCN7cVgb4Vq7U/H50Pq4JNP7Qiw8UFnJwcK+tXy+Wj6PLEvPgHSHv5UgwA1IQIwwyFAyLJin9RoxYgAzAQIkPwNmf26busC+OIx5TDqo5nDT+F/SS/9CYzwb+No49zNy2evkYv0LywGGAXUvp6eSneycqOic0w20k7CNgKE7jJunSGLACTCxF27ylmQc98T5MQUH49swd+I0HPXslLKnT0N+wnkrTKi9JZL/L9i1SorMmdeQ4TQQ7OFMxIMzGD45w8nUL1im7efENZLJpgPSw0pfz0cdt4U3230Td/Tvx2R6d2FrHhEWLkq5PELOMsRPHCPnAZGv1xJteL7jbJiaW3sB2nDvPC/osSYvjRQz4cJ6n7KO3rYQL7M+L6nVtfDVRAEQRAEQRAEQRAEIZ5/SAXmdfXaoQsAAAAASUVORK5CYII=&longCache=true" ></a>

__@MC着火的冰块__，传送门：[空降至Bilibili](https://space.bilibili.com/551409211 "点击空降")

## 简介

> 最近谷歌翻译在网上火了，因为谷歌翻译是机器翻译，所以如果只是翻译一次，大体还是有九成九的准确度的，但是当使用谷歌翻译选择小语种，然后小语种再翻译到另一个小语种，重复翻译多遍后，内容就会疯狂失真，然后准确度也会随着翻译次数开始偏离原来的真正的意思。  

__可如果手动翻译效率极低，于是就有了这款自动翻译机__

自从2022年10月，谷歌翻译退出中国大陆后，旧版的谷歌生草机就不再能使用。于是在本程序中，集成了[GoogleTranslateIpCheck](https://github.com/Ponderfly/GoogleTranslateIpCheck)，可以扫描国内可用的谷歌翻译IP。

## 与旧版相比的优点

- 采用更合理的算法（多协程），不仅提高了效率，还降低了CPU消耗，界面更流畅
- 文本之间可以一一对应，更方便做视频
- 用GoogleTranslateIpCheck代替镜像网站，连接更稳定，操作更方便

## 支持的功能

- [x] 逐句翻译，一一对应
- [x] 设置分隔符、翻译次数、超时、出错自动重试次数
- [x] 下载音频
- [x] 一键使用GoogleTranslateIpCheck
- [x] 自定义使用的语言
