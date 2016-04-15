# -*- coding: utf-8 -*-
import os
import gettext

APP_NAME = "i18n_demo"
LOCALE_DIR = os.path.abspath("locale")

# 这条语句会将_()函数自动放到python的内置命名空间中
gettext.install(APP_NAME, LOCALE_DIR)
# 获取简体中文翻译类的实例
lang_cn = gettext.translation(APP_NAME, LOCALE_DIR, ["cn"])
# 获取英文翻译类的实例
lang_en = gettext.translation(APP_NAME, LOCALE_DIR, ["en"])

if __name__ == "__main__":
    # 安装中文
    lang_cn.install()
    print _('This is a translatable string.')

    # 安装英文（程序中实时切换回英文）
    lang_en.install()
    print _('This is a translatable string.')
