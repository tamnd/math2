---
records:
    - id: QFJ6WK5Q50
      kind: problem-set
      title: Kvant 1982, no. 7
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1982"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1982"
          structure: QFJ6WK5Q50/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1982-7
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
    - id: QFJZEFXKDB
      kind: monograph
      title: Toric Varieties
      creators:
        - name: David Cox
          role: author
        - name: John Little
          role: author
        - name: Henry Schenck
          role: author
      date: "2011-07-07"
      msc:
        - code: 14-01
          from: zbmath_search
        - code: 14M25
          from: zbmath_search
        - code: 14C17
          from: zbmath_search
        - code: 14C15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2011-07-07"
          ids:
            doi: 10.1090/gsm/124
            zbl: "1223.14001"
            zbl_id: "5934474"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2011-07-07"
              ids:
                isbn:
                    - "9780821848197"
                    - "9780821884263"
                    - "9781470411855"
              access:
                class: record
      relations:
        - kind: part_of
          to: YBEDX3XNVA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/gsm/124
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5934474"
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
---
