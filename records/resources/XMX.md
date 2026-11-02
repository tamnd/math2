---
records:
    - id: XMXJFE5NNE
      kind: monograph
      title: Categories for the Working Mathematician
      creators:
        - name: Saunders Mac Lane
          role: author
      date: "1971"
      msc:
        - code: 18-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1971"
          ids:
            doi:
                - 10.1007/978-1-4612-9839-7
                - 10.1007/978-1-4757-4721-8
            zbl: "0232.18001"
            zbl_id: "3367095"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1971"
              ids:
                isbn:
                    - "9780387900360"
                    - "9781461298397"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1978"
              ids:
                isbn:
                    - "9781441931238"
                    - "9781475747218"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.17 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-9839-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-4721-8
          level: work
        - source: zbmath_search
          snapshot: blake3:ba52b67aca79888bd54f4ac0d57bd446df8c82ca03dd9e92e0bc9db1402905ce
          native_id: "3367095"
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
