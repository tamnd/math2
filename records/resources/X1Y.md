---
records:
    - id: X1Y0AKAGZX
      kind: monograph
      title: Geometry of Polynomials
      creators:
        - name: Morris Marden
          role: author
      date: "1949-12-31"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1949-12-31"
          ids:
            doi: 10.1090/surv/003
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1949-12-31"
              ids:
                isbn:
                    - "9780821815038"
                    - "9781470412302"
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
          native_id: 10.1090/surv/003
          level: work
        - source: crossref_language
          snapshot: blake3:8055274d703e6bb5b000d2e6eff227662c304b1de00a456a1218f6424b926f45
          native_id: 10.1090/surv/003
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: X1YF62ZFB6
      kind: preprint
      title: Coloring 3-colorable graphs with $O(n^{4/23})$ colors via a Gaussian-cover recursion
      creators:
        - name: Emile Anand
          role: author
      date: "2026-10-01"
      subjects:
        - system: arxiv
          code: cs.DS
        - system: arxiv
          code: cs.CC
        - system: arxiv
          code: cs.DM
        - system: arxiv
          code: math.CO
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-01"
          ids:
            arxiv: "2610.01071"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.01071"
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
