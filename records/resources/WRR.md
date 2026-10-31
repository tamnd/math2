---
records:
    - id: WRRPJ56917
      kind: preprint
      title: Particle-based algorithm for stochastic optimal control
      creators:
        - name: Sebastian Reich
          role: author
      date: "2023-11-12"
      subjects:
        - system: arxiv
          code: math.OC
        - system: arxiv
          code: cs.NA
        - system: arxiv
          code: math.NA
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2023-11-12"
          ids:
            arxiv: "2311.06906"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2311.06906"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: WRRVZHM9JW
      kind: monograph
      title: A Study in Derived Algebraic Geometry
      creators:
        - name: Dennis Gaitsgory
          role: author
        - name: Nick Rozenblyum
          role: author
      date: "2017-07-06"
      expressions:
        - key: e1
          kind: edition
          date: "2017-07-06"
          ids:
            doi:
                - 10.1090/surv/221.1
                - 10.1090/surv/221.2
          manifestations:
            - key: m1
              kind: print
              publisher: |-
                American Mathematical
                                    Society
              date: "2017-07-06"
              ids:
                isbn:
                    - "9781470435691"
                    - "9781470440855"
            - key: m2
              kind: print
              publisher: |-
                American Mathematical
                                    Society
              date: "2017-08-29"
              ids:
                isbn:
                    - "9781470435707"
                    - "9781470440879"
      relations:
        - kind: part_of
          to: M891DMMNP3
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/221.1
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/221.2
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
