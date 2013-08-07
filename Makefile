.PHONY: init
init: clone-gaia hg-init

.PHONY: update
update: update-gaia update-hg

.PHONY: add-locales
add-locales:
	mkdir -p locales
	./locales.sh add $(LOCALES)

.PHONY: remove-locales
remove-locales:
	./locales.sh remove $(LOCALES)

.PHONY: find-dupl-locales
find-dupl-locales:
	./locales.sh dupl $(LOCALES)

.PHONY: clone-gaia
clone-gaia:
	git clone https://github.com/mozilla-b2g/gaia $<
	git --git-dir=gaia/.git --work-tree=gaia/ checkout v1-train

.PHONY: hg-init
hg-init:
	./locales.sh init $(LOCALES)

.PHONY: update-gaia
update-gaia:
	git --git-dir=gaia/.git fetch
	git --git-dir=gaia/.git --work-tree=gaia/ merge origin/v1-train

.PHONY: update-hg
update-hg:
	./locales.sh update $(LOCALES)
