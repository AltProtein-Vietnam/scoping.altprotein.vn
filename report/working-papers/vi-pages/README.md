# Vietnamese pages held back from v0.10

The Vietnamese executive summary (*Tóm tắt báo cáo*, `front-exec-summary-vi`) and the Vietnamese prologue (*Lời mở đầu*, `front-prologue-vi`) left the package in version 0.10. A full translation pass is planned once version 1.0 is done, so these files keep their v0.10 texts as a starting point. They are not published, are not in `site-manifest.json`, and are not checked by `tools/validate.py`.

To bring a page back: move it to `content/00-front/`, add it to `pages`, `nav` and `audience_paths` (`vietnamese-readers`) in `site-manifest.json`, restore the links listed in Appendix M5, section M5.16, and run both checks.

The bilingual glossary (Appendix R3) and the Vietnamese tile labels (`label_vi` in `data/key-numbers.json`) stay in the package.
