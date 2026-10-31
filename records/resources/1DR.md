---
records:
    - id: 1DRD5FAJ4C
      kind: preprint
      title: Zeros and Their Distribution for Leonardo Polynomials
      creators:
        - name: Muhammet Karagöz
          role: author
        - name: Nihal Özgür
          role: author
      date: "2026-10-08"
      subjects:
        - system: arxiv
          code: math.GM
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-08"
          ids:
            arxiv: "2610.14080"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.14080"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: 1DRF7A6BKV
      kind: monograph
      title: 'Categorical Aspects of Topology and Analysis: Proceedings of an International Conference Held at Carleton University, Ottawa, August 11–15, 1981'
      creators:
        - name: B. Banaschewski
          role: editor
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          ids:
            doi: 10.1007/bfb0092866
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540112112"
                    - "9783540390411"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0092866
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
