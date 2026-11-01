---
records:
    - id: Y3H0ATFFBC
      kind: monograph
      title: Extinction and Quasi-Stationarity in the Stochastic Logistic SIS Model
      creators:
        - name: Ingemar Nåsell
          role: author
      date: "2011"
      msc:
        - code: 92-02
          from: zbmath_search
        - code: 92D30
          from: zbmath_search
        - code: 60J20
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2011"
          ids:
            doi: 10.1007/978-3-642-20530-9
            zbl: "1320.92019"
            zbl_id: "5883028"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2011"
              ids:
                isbn:
                    - "9783642205293"
                    - "9783642205309"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-20530-9
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5883028"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: Y3HBJMCC4D
      kind: preprint
      title: Cryptanalysis of a Class of Ideal Secret Sharing Schemes Based on the CRT for Polynomial Rings
      creators:
        - name: Jian Ding
          role: author
        - name: Zhiyuan Guo
          role: author
        - name: Hongju Li
          role: author
        - name: Yuying Man
          role: author
      date: "2026-10-05"
      subjects:
        - system: arxiv
          code: cs.CR
        - system: arxiv
          code: cs.IT
        - system: arxiv
          code: math.IT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-05"
          ids:
            arxiv: "2610.06312"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.06312"
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
