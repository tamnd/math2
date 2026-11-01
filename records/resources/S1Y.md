---
records:
    - id: S1YAVPV2KR
      kind: problem-set
      title: Kvant 1972, no. 1
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1972"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1972"
          structure: S1YAVPV2KR/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1972-1
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
    - id: S1YEDRFJC7
      kind: edited-volume
      title: Wavelets, Multiwavelets, and Their Applications
      creators:
        - name: Akram Aldroubi
          role: editor
        - name: EnBing Lin
          role: editor
      date: "1998"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 42-06
          from: zbmath_search
        - code: 65-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1998"
          ids:
            doi: 10.1090/conm/216
            zbl: "0884.00041"
            zbl_id: "1130221"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1998"
              ids:
                isbn:
                    - "9780821807934"
                    - "9780821855522"
                    - "9780821878088"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/216
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1130221"
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
