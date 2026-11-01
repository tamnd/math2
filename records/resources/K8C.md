---
records:
    - id: K8C5GZ1TKH
      kind: monograph
      title: Geometry of Hypersurfaces
      creators:
        - name: Thomas E. Cecil
          role: author
        - name: Patrick J. Ryan
          role: author
      date: "2015"
      msc:
        - code: 53-02
          from: zbmath_search
        - code: 53A07
          from: zbmath_search
        - code: 53C40
          from: zbmath_search
        - code: 53C42
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2015"
          ids:
            doi: 10.1007/978-1-4939-3246-7
            zbl: "1331.53001"
            zbl_id: "6482001"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2015"
              ids:
                isbn:
                    - "9781493932450"
                    - "9781493932467"
              access:
                class: record
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4939-3246-7
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "6482001"
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
    - id: K8CQDCYBR3
      kind: preprint
      title: A Dynamic Sampling Adaptive-SGD Method for Machine Learning
      creators:
        - name: Achraf Bahamou
          role: author
        - name: Donald Goldfarb
          role: author
      date: "2019-12-31"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
        - system: arxiv
          code: stat.ML
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2019-12-31"
          ids:
            arxiv: "1912.13357"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "1912.13357"
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
