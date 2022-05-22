all:
	@echo "No default target."

icons:
	pyrcc5 -o simsapa/assets/icons_rc.py simsapa/assets/icons.qrc

ui:
	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/sutta_search_window_ui.py simsapa/assets/ui/sutta_search_window.ui && \
	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/sutta_study_window_ui.py simsapa/assets/ui/sutta_study_window.ui && \
	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/dictionary_search_window_ui.py simsapa/assets/ui/dictionary_search_window.ui && \
	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/memos_browser_window_ui.py simsapa/assets/ui/memos_browser_window.ui && \
	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/links_browser_window_ui.py simsapa/assets/ui/links_browser_window.ui

#	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/dictionaries_manager_window_ui.py simsapa/assets/ui/dictionaries_manager_window.ui && \
#	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/document_reader_window_ui.py simsapa/assets/ui/document_reader_window.ui && \
#	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/library_browser_window_ui.py simsapa/assets/ui/library_browser_window.ui && \
#	pyuic5 --import-from=simsapa.assets -o simsapa/assets/ui/import_stardict_dialog_ui.py simsapa/assets/ui/import_stardict_dialog.ui

sass-build:
	sass --no-source-map './simsapa/assets/sass/:./simsapa/assets/css/'

sass-watch:
	sass --no-source-map --watch './simsapa/assets/sass/:./simsapa/assets/css/'

tests:
	USE_TEST_DATA=true pytest tests/

bootstrap-appdata:
	./scripts/bootstrap-appdata.sh

count-code:
	tokei --type Python --exclude simsapa/assets/ --exclude simsapa/keyboard/ . | grep -vE '===|Total'
