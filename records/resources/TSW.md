---
records:
    - id: TSW492DDHQ
      kind: monograph
      title: 'The Real Numbers: An Introduction to Set Theory and Analysis'
      creators:
        - name: John Stillwell
          role: author
      date: "2013"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 26A03
          from: zbmath_search
        - code: "03E10"
          from: zbmath_search
        - code: 01A05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2013"
          ids:
            doi: 10.1007/978-3-319-01577-4
            zbl: "1292.26004"
            zbl_id: "6210195"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2013"
              ids:
                isbn:
                    - "9783319015767"
                    - "9783319015774"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-01577-4
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "6210195"
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
