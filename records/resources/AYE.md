---
records:
    - id: AYEPND6TAA
      kind: monograph
      title: A Readable Introduction to Real Mathematics
      creators:
        - name: Daniel Rosenthal
          role: author
        - name: David Rosenthal
          role: author
        - name: Peter Rosenthal
          role: author
      date: "2014"
      msc:
        - code: 00-01
          from: zbmath_search
        - code: 00A05
          from: zbmath_search
        - code: 00A35
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2014"
          ids:
            doi:
                - 10.1007/978-3-030-00632-7
                - 10.1007/978-3-319-05654-8
            zbl: "1358.00003"
            zbl_id: "6292992"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783030006310"
                    - "9783030006327"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2014"
              ids:
                isbn:
                    - "9783319056531"
                    - "9783319056548"
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
          native_id: 10.1007/978-3-030-00632-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-05654-8
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "6292992"
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
