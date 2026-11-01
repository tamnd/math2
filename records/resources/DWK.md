---
records:
    - id: DWKRSJ97AS
      kind: monograph
      title: Invariant Theory of Finite Groups
      creators:
        - name: Mara Neusel
          role: author
        - name: Larry Smith
          role: author
      date: "2010-03-08"
      msc:
        - code: 20-XX
          from: classify/1@2b838f8bc9d8
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010-03-08"
          ids:
            doi: 10.1090/surv/094
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2010-03-08"
              ids:
                isbn:
                    - "9780821849811"
                    - "9781470413217"
              access:
                class: record
      relations:
        - kind: part_of
          to: M891DMMNP3
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/094
          level: work
        - source: crossref_language
          snapshot: blake3:8055274d703e6bb5b000d2e6eff227662c304b1de00a456a1218f6424b926f45
          native_id: 10.1090/surv/094
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: DWKWF242Y0
      kind: preprint
      title: Grokking through the Lens of Minimum-Norm Interpolation
      creators:
        - name: Gil Kur
          role: author
        - name: Ileana Rugina
          role: author
        - name: Clémentine Carla Juliette Dominé
          role: author
        - name: Marco Mondelli
          role: author
      date: "2026-09-29"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-29"
          ids:
            arxiv: "2609.38453"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.38453"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
---
