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
        by: m2 dev scope/1
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
      msc:
        - code: 47-02
          from: zbmath_search
        - code: 47A08
          from: zbmath_search
        - code: 47A05
          from: zbmath_search
        - code: 47A10
          from: zbmath_search
        - code: 47A53
          from: zbmath_search
        - code: 47A55
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2022-06-07"
          ids:
            doi: 10.1090/surv/267
            zbl: "1509.47001"
            zbl_id: "7550580"
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
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/267
          level: work
        - source: crossref_language
          snapshot: blake3:99510ada1a0f54f83dbf4ed97ef48852461d1f98d338d1a350cabf222fb85948
          native_id: 10.1090/surv/267
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "7550580"
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
          at: "2026-11-02"
          by: m2 v0.6.17 scope/1
          note: from in to in
---
