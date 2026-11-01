---
records:
    - id: S9TW513T5Y
      kind: problem-set
      title: Putnam 1995
      creators:
        - name: Mathematical Association of America
          role: author
      date: "1995"
      msc:
        - code: 00A07
          from: putnam
        - code: 97U40
          from: putnam
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1995"
          structure: S9TW513T5Y/e1.json
      relations:
        - kind: part_of
          to: TYDZDDC2MA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: putnam
          snapshot: blake3:a8efce689e279311a280a90aaaac925d4b96f7c8ccdd9eb1e8fb29b48d574603
          native_id: "1995"
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
    - id: S9TYMAFQM0
      kind: monograph
      title: Completion Problems on Operator Matrices
      creators:
        - name: Dragana Cvetković Ilić
          role: author
      date: "2022-06-07"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2022-06-07"
          ids:
            doi: 10.1090/surv/267
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2022-06-07"
              ids:
                isbn:
                    - "9781470471132"
                    - "9781470469870"
              access:
                class: record
      relations:
        - kind: part_of
          to: M891DMMNP3
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/267
          level: work
        - source: crossref_language
          snapshot: blake3:78a08c6dff20a47d6ad06a8fc0424f997c851421644ee012bc0f425814d0a6d5
          native_id: 10.1090/surv/267
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
