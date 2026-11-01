---
records:
    - id: DHFF3KSC2C
      kind: monograph
      title: Probability and Statistical Inference
      creators:
        - name: J. G. Kalbfleisch
          role: author
      date: "1979"
      msc:
        - code: 60-01
          from: zbmath_search
        - code: 60-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1979"
          ids:
            doi:
                - 10.1007/978-1-4684-0089-2
                - 10.1007/978-1-4684-0091-5
            zbl: "0418.60004"
            zbl_id: "3651449"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1979"
              ids:
                isbn:
                    - "9780387904573"
                    - "9781468400892"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer US
              date: "1979"
              ids:
                isbn:
                    - "9780387904580"
                    - "9781468400915"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0089-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0091-5
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3651449"
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
