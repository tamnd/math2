---
records:
    - id: T7R1Q29DQK
      kind: preprint
      title: An Accuracy-Information Tradeoff for Loss-Difference Conditional Mutual Information
      creators:
        - name: Hazar Yueksel
          role: author
      date: "2026-10-06"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: cs.IT
        - system: arxiv
          code: math.IT
        - system: arxiv
          code: stat.ML
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-06"
          ids:
            arxiv: "2610.09206"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.09206"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: T7RD68SZGZ
      kind: edited-volume
      title: Mexican Mathematicians in the World
      creators:
        - name: Fernando Galaz-García
          role: editor
        - name: Cecilia González-Tokman
          role: editor
        - name: Juan Pardo Millán
          role: editor
      date: "2021-12-07"
      msc:
        - code: 00-XX
          from: classify/1@2b838f8bc9d8
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2021-12-07"
          ids:
            doi: 10.1090/conm/775
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2021-12-07"
              ids:
                isbn:
                    - "9781470467289"
                    - "9781470465360"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/775
          level: work
        - source: crossref_language
          snapshot: blake3:78a08c6dff20a47d6ad06a8fc0424f997c851421644ee012bc0f425814d0a6d5
          native_id: 10.1090/conm/775
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
