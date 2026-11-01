---
records:
    - id: M7H8NFY4WH
      kind: course
      title: Set Theory and Mathematical Logic
      creators:
        - name: Amit Kuber
          role: instructor
      msc:
        - code: 03-XX
          from: classify/1@2b838f8bc9d8
      ids:
        course: 05pjsgx75:111104416
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Kanpur
              ids:
                nptel: "111104416"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111104416"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: M7HDZGSCJD
      kind: monograph
      title: Symmetry Breaking for Representations of Rank One Orthogonal Groups II
      creators:
        - name: Toshiyuki Kobayashi
          role: author
        - name: Birgit Speh
          role: author
      date: "2018"
      msc:
        - code: 22-02
          from: zbmath_search
        - code: "22E30"
          from: zbmath_search
        - code: "22E45"
          from: zbmath_search
        - code: "22E46"
          from: zbmath_search
        - code: 58J70
          from: zbmath_search
        - code: 81R40
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2018"
          ids:
            doi: 10.1007/978-981-13-2901-2
            zbl: "1421.81003"
            zbl_id: "6967938"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Singapore
              date: "2018"
              ids:
                isbn:
                    - "9789811329005"
                    - "9789811329012"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-981-13-2901-2
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "6967938"
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
          by: m2 v0.6.14 scope/1
          note: from in to in
---
