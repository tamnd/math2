---
records:
    - id: BAXMWJSQ0W
      kind: problem-set
      title: Kvant 2022, no. 1
      creators:
        - name: Kvant editorial board
          role: editor
      date: "2022"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "2022"
          structure: BAXMWJSQ0W/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2022-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: BAXPRZJTJV
      kind: edited-volume
      title: Theta Functions–Bowdoin 1987
      creators:
        - name: Leon Ehrenpreis
          role: editor
        - name: Robert Gunning
          role: editor
      date: "1989"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1989"
          ids:
            doi:
                - 10.1090/pspum/049.1
                - 10.1090/pspum/049.2
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1989"
              ids:
                isbn:
                    - "9780821814833"
                    - "9780821868140"
                    - "9780821893449"
              access:
                class: record
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "1989"
              ids:
                isbn:
                    - "9780821814840"
                    - "9780821868157"
                    - "9780821893456"
              access:
                class: record
      relations:
        - kind: part_of
          to: EVG9FMRY3R
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/pspum/049.1
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/pspum/049.2
          level: work
        - source: crossref_language
          snapshot: blake3:8055274d703e6bb5b000d2e6eff227662c304b1de00a456a1218f6424b926f45
          native_id: 10.1090/pspum/049.1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
