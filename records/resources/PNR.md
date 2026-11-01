---
records:
    - id: PNRHHWGHM2
      kind: preprint
      title: Bayesian Interpolation with Deep Linear Networks
      creators:
        - name: Boris Hanin
          role: author
        - name: Alexander Zlokapa
          role: author
      date: "2022-12-29"
      subjects:
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2022-12-29"
          ids:
            arxiv: "2212.14457"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2212.14457"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: PNRNKZ79KM
      kind: monograph
      title: Ideals of Identities of Associative Algebras
      creators:
        - name: Aleksander Kemer
          role: author
      date: "1991-06-06"
      msc:
        - code: 16-02
          from: zbmath_search
        - code: 16Rxx
          from: zbmath_search
        - code: 16R10
          from: zbmath_search
        - code: 16W50
          from: zbmath_search
        - code: 16W55
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1991-06-06"
          ids:
            doi: 10.1090/mmono/087
            zbl: "0732.16001"
            zbl_id: "50288"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1991-06-06"
              ids:
                isbn:
                    - "9780821845486"
                    - "9780821898291"
                    - "9781470444990"
              access:
                class: record
      relations:
        - kind: part_of
          to: BTDY0N3WC9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/087
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "50288"
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
